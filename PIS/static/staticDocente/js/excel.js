let unidadData = {};

function downloadExcel() {
    const workbook = XLSX.utils.book_new();

    for (let unidad = 1; unidad <= 3; unidad++) {
        if (unidadData[`unidad${unidad}`]) {
            const worksheet = XLSX.utils.json_to_sheet(unidadData[`unidad${unidad}`]);
            XLSX.utils.book_append_sheet(workbook, worksheet, `Unidad ${unidad}`);
        }
    }

    const finalData = [];
    const students = {};

    for (let unidad = 1; unidad <= 3; unidad++) {
        if (unidadData[`unidad${unidad}`]) {
            unidadData[`unidad${unidad}`].forEach(row => {
                const key = `${row.Nombre} ${row.Apellido}`;

                if (!students[key]) {
                    students[key] = {
                        Id: row.Id,
                        Nombre: row.Nombre,
                        Apellido: row.Apellido,
                        Matricula: row.Matricula,
                        promedios: [null, null, null],
                        comentarios: [null, null, null]
                    };
                }

                students[key].promedios[unidad - 1] = calcularPromedio(row);
                students[key].comentarios[unidad - 1] = row.Comentario || '';
            });
        }
    }

    for (const [key, info] of Object.entries(students)) {
        const promedioFinal = info.promedios.filter(p => p !== null).reduce((a, b) => a + b, 0) / info.promedios.filter(p => p !== null).length;
        const categoriaFinal = obtenerCategoria(promedioFinal);
        const necesitaSupletorio = info.promedios.some(promedio => promedio < 7) ? 'Sí' : 'No';
        finalData.push({
            'Id': info.Id,
            'Nombre': info.Nombre,
            'Apellido': info.Apellido,
            'Matricula': info.Matricula,
            'Promedio Unidad 1': info.promedios[0] !== null ? info.promedios[0].toFixed(2) : 'N/A',
            'Promedio Unidad 2': info.promedios[1] !== null ? info.promedios[1].toFixed(2) : 'N/A',
            'Promedio Unidad 3': info.promedios[2] !== null ? info.promedios[2].toFixed(2) : 'N/A',
            'Promedio Final': promedioFinal.toFixed(2),
            'Categoría Final': categoriaFinal.text,
            'Supletorio': necesitaSupletorio,
        });
    }

    const finalWorksheet = XLSX.utils.json_to_sheet(finalData);
    XLSX.utils.book_append_sheet(workbook, finalWorksheet, 'Resumen Final');

    XLSX.writeFile(workbook, 'Reporte_Estudiantes.xlsx');
}

function calcularPromedio(row) {
    const notas = Object.keys(row).filter(key => key.startsWith('Nota')).map(key => row[key]);
    const suma = notas.reduce((acc, nota) => acc + nota, 0);
    return suma / notas.length;
}

function obtenerCategoria(promedio) {
    if (promedio >= 8.5) return { text: 'A', color: 'category-a' };
    if (promedio >= 7.5) return { text: 'B', color: 'category-b' };
    if (promedio >= 5) return { text: 'C', color: 'category-c' };
    return { text: 'D', color: 'category-d' };
}

function uploadExcel(unidad) {
    document.getElementById(`file-upload-${unidad}`).click();
}

function handleFileSelect(unidad) {
    const fileInput = document.getElementById(`file-upload-${unidad}`);
    if (fileInput.files.length > 0) {
        updateExcelButton(unidad, true);
        handleFileUpload(unidad, fileInput.files[0]);
    }
}

function updateExcelButton(unidad, fileUploaded) {
    const button = document.getElementById(`upload-button-${unidad}`);
    if (fileUploaded) {
        button.textContent = `Actualizar Excel para Unidad ${unidad}`;
        button.classList.add('file-uploaded');
    } else {
        button.textContent = `Elegir Excel para Unidad ${unidad}`;
        button.classList.remove('file-uploaded');
    }
}

function handleFileUpload(unidad, file) {
    const reader = new FileReader();
    reader.onload = function (e) {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const json = XLSX.utils.sheet_to_json(worksheet);

        json.forEach(row => {
            row.Promedio = calcularPromedio(row);
            row.Categoria = obtenerCategoria(row.Promedio).text;
            row.Comentario = row.Comentario || '';
        });

        unidadData[`unidad${unidad}`] = json;

        updateTable(unidad, json);

        if (Object.keys(unidadData).length === 3) {
            createFinalTable();
        }
    };
    reader.readAsArrayBuffer(file);
}

function updateTable(unidad, data) {
    const tableContainer = document.getElementById(`table-container-${unidad}`);
    tableContainer.innerHTML = '';
    const table = document.createElement('table');
    table.classList.add('results-table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    const notasColumns = Object.keys(data[0]).filter(key => key.startsWith('Nota') && !isNaN(data[0][key]));

    thead.innerHTML = `
<tr>
    <th>ID</th>
    <th>Matricula</th>
    <th>Nombre</th>
    <th>Apellido</th>
    ${notasColumns.map(col => `<th>${col}</th>`).join('')}
    <th>Promedio</th>
    <th>Categoría</th>
    <th>Observaciones</th>
    <th>Acciones</th>
</tr>
`;

    data.forEach(row => {
        const matriculaClass = `matricula-${row.Matricula}`;
        const rowElement = document.createElement('tr');
        rowElement.innerHTML = `
    <td>${row.Id}</td>
    <td class="${matriculaClass}">${row.Matricula}</td>    
    <td>${row.Nombre}</td>
    <td>${row.Apellido}</td>
    ${notasColumns.map(col => `<td>${row[col]}</td>`).join('')}
    <td>${row.Promedio.toFixed(2)}</td>
    <td class="category-${row.Categoria.toLowerCase()}">${row.Categoria}</td>
    <td>${row.Comentario || ''}</td>
    <td class="action-buttons">
        <button class="action-button update-btn" onclick="updateStudent('${row.Id}')">
            <i class="bx bx-edit"></i>
        </button>
        <button class="action-button delete-btn" onclick="deleteStudent('${row.Id}')">
            <i class="bx bx-trash"></i>
        </button>
        <button onclick="addComment(${unidad}, '${row.Id}')">Observacion</button>
        <button onclick="getPrediction('${row.Id}')">Proyeccion</button>
    </td>
    </td>
`;
        tbody.appendChild(rowElement);
    });

    table.appendChild(thead);
    table.appendChild(tbody);
    tableContainer.appendChild(table);

    const buttonContainer = document.createElement('div');
    buttonContainer.classList.add('button-container');
    buttonContainer.innerHTML = `
<button class="action-button download-btn" onclick="downloadExcelUnit(${unidad})">
    <i class="bx bx-download"></i> Descargar Excel Unidad ${unidad}
</button>
<button class="action-button send-btn" onclick="sendReport(${unidad})">
    <i class="bx bx-send"></i> Enviar Datos Unidad ${unidad}
</button>
`;
    tableContainer.appendChild(buttonContainer);

    checkAllUnitsUploaded();
}

function checkAllUnitsUploaded() {
    if (Object.keys(unidadData).length === 3) {
        const finalButtonsContainer = document.getElementById('buttons-container');
        finalButtonsContainer.innerHTML = `
    <button class="action-button download-btn" onclick="downloadExcel()">
        <i class="bx bx-download"></i> Descargar Excel
    </button>
    <button class="action-button send-btn" onclick="sendReport('final')">
        <i class="bx bx-send"></i> Enviar reporte final
    </button>
`;
        finalButtonsContainer.style.display = 'flex';
    }
}

function addComment(unidad, id) {
    Swal.fire({
        title: 'Ingrese el correo electrónico y comentario para este estudiante:',
        html: `
    <input type="email" id="studentEmail" class="swal2-input" placeholder="Correo electrónico">
    <textarea id="studentComment" class="swal2-textarea" placeholder="Comentario" aria-label="Escribe tu comentario aquí"></textarea>
`,
        focusConfirm: false,
        showCancelButton: true,
        confirmButtonText: 'Enviar',
        cancelButtonText: 'Cancelar',
        preConfirm: () => {
            const email = Swal.getPopup().querySelector('#studentEmail').value;
            const comment = Swal.getPopup().querySelector('#studentComment').value;
            if (!email || !comment) {
                Swal.showValidationMessage('¡El correo electrónico y el comentario no pueden estar vacíos!');
            }
            return { email: email, comment: comment };
        }
    }).then((result) => {
        if (result.isConfirmed) {
            const { email, comment } = result.value;
            // Guardar el comentario en la estructura de datos
            if (!unidadData[`unidad${unidad}`]) {
                unidadData[`unidad${unidad}`] = [];
            }
            const studentIndex = unidadData[`unidad${unidad}`].findIndex(s => s.Id.toString() === id);
            if (studentIndex !== -1) {
                unidadData[`unidad${unidad}`][studentIndex].Comentario = comment;
                updateTable(unidad, unidadData[`unidad${unidad}`]);
            }
            // Enviar el correo electrónico
            sendEmail(email, comment);
        }
    });
}

function sendEmail(email, comment) {
    emailjs.send('your_service_id', 'your_template_id', {
        to_email: email,
        message: comment
    })
        .then((response) => {
            console.log('Correo enviado exitosamente!', response.status, response.text);
        }, (error) => {
            console.error('Error al enviar el correo:', error);
        });
}



function downloadExcelUnit(unidad) {
    const workbook = XLSX.utils.book_new();
    const data = unidadData[`unidad${unidad}`].map(row => {
        const newRow = {
            Id: row.Id,
            Matricula: row.Matricula,
            Nombre: row.Nombre,
            Apellido: row.Apellido,
        };
        Object.keys(row).filter(key => key.startsWith('Nota') && !isNaN(row[key])).forEach(key => {
            newRow[key] = row[key];
        });
        newRow.Promedio = row.Promedio;
        newRow.Categoria = row.Categoria;
        return newRow;
    });
    const worksheet = XLSX.utils.json_to_sheet(data);
    XLSX.utils.book_append_sheet(workbook, worksheet, `Unidad ${unidad}`);
    XLSX.writeFile(workbook, `Reporte_Unidad_${unidad}.xlsx`);
}

function sendDataUnit(unidad) {
    console.log(`Enviando datos de Unidad ${unidad}:`, unidadData[`unidad${unidad}`]);
    alert(`Datos de Unidad ${unidad} enviados correctamente`);
}

function createFinalTable() {
    const finalTableContainer = document.createElement('div');
    finalTableContainer.id = 'final-table-container';
    finalTableContainer.innerHTML = '<h2>Tabla Final</h2>';

    const table = document.createElement('table');
    table.classList.add('results-table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    thead.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Matricula</th>
            <th>Promedio Unidad 1</th>
            <th>Promedio Unidad 2</th>
            <th>Promedio Unidad 3</th>
            <th>Promedio Final</th>
            <th>Categoría Final</th>
            <th>Supletorio</th>
        </tr>
    `;

    const students = {};

    for (let unidad = 1; unidad <= 3; unidad++) {
        if (unidadData[`unidad${unidad}`]) {
            unidadData[`unidad${unidad}`].forEach(row => {
                const key = `${row.Nombre} ${row.Apellido}`;

                if (!students[key]) {
                    students[key] = {
                        Id: row.Id,
                        Nombre: row.Nombre,
                        Apellido: row.Apellido,
                        Matricula: row.Matricula,
                        promedios: [null, null, null]
                    };
                }

                students[key].promedios[unidad - 1] = row.Promedio;
            });
        }
    }

    Object.entries(students).forEach(([key, info]) => {
        const promedioFinal = info.promedios.filter(p => p !== null).reduce((a, b) => a + b, 0) / info.promedios.filter(p => p !== null).length;
        const categoriaFinal = obtenerCategoria(promedioFinal);
        const necesitaSupletorio = info.promedios.some(promedio => promedio < 7) ? 'Sí' : 'No';

        const rowElement = document.createElement('tr');
        rowElement.innerHTML = `
            <td>${info.Id}</td>
            <td>${info.Nombre}</td>
            <td>${info.Apellido}</td>
            <td>${info.Matricula}</td>
            <td>${info.promedios[0] !== null ? info.promedios[0].toFixed(2) : 'N/A'}</td>
            <td>${info.promedios[1] !== null ? info.promedios[1].toFixed(2) : 'N/A'}</td>
            <td>${info.promedios[2] !== null ? info.promedios[2].toFixed(2) : 'N/A'}</td>
            <td>${promedioFinal.toFixed(2)}</td>
            <td class="${categoriaFinal.color}">${categoriaFinal.text}</td>
            <td   td>${necesitaSupletorio}</td>
        `;
        tbody.appendChild(rowElement);
    });

    table.appendChild(thead);
    table.appendChild(tbody);
    finalTableContainer.appendChild(table);

    document.querySelector('.units-container').appendChild(finalTableContainer);
}

function deleteStudent(id) {
    for (let unidad = 1; unidad <= 3; unidad++) {
        if (unidadData[`unidad${unidad}`]) {
            unidadData[`unidad${unidad}`] = unidadData[`unidad${unidad}`].filter(student => student.Id.toString() !== id);
            updateTable(unidad, unidadData[`unidad${unidad}`]);
        }
    }
    if (Object.keys(unidadData).length === 3) {
        createFinalTable();
    }
}

function applyFilter() {
    const category = document.getElementById('average-select').value;
    const matricula = document.getElementById('matricula-select').value;

    let filteredData = [];
    for (let unidad = 1; unidad <= 3; unidad++) {
        if (unidadData[`unidad${unidad}`]) {
            const unitFilteredData = unidadData[`unidad${unidad}`].filter(student => {
                return (!category || student.Categoria === category) &&
                    (!matricula || student.Matricula.toString() === matricula);
            });
            filteredData = filteredData.concat(unitFilteredData.map(student => ({ ...student, Unidad: unidad })));
        }
    }

    updateTableWithFilter(filteredData);
}

function updateTableWithFilter(data) {
    const tableContainer = document.getElementById('filtered-results-container');
    tableContainer.innerHTML = '';

    if (data.length === 0) {
        tableContainer.innerHTML = '<p>No se encontraron resultados.</p>';
        return;
    }

    const table = document.createElement('table');
    table.classList.add('results-table');

    const thead = document.createElement('thead');
    thead.innerHTML = `
<tr>
    <th>Matricula</th>
    <th>Nombre</th>
    <th>Apellido</th>
    <th>Promedio</th>
    <th>Categoría</th>
    <th>Unidad</th>
</tr>
`;

    const tbody = document.createElement('tbody');

    data.forEach(student => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
    <td>${student.Matricula}</td>
    <td>${student.Nombre}</td>
    <td>${student.Apellido}</td>
    <td>${student.Promedio.toFixed(2)}</td>
    <td class="category-${student.Categoria.toLowerCase()}">${student.Categoria}</td>
    <td>Unidad ${student.Unidad}</td>
`;
        tbody.appendChild(tr);
    });

    table.appendChild(thead);
    table.appendChild(tbody);
    tableContainer.appendChild(table);
}

function sendReport(type) {
    const cycleSelect = document.getElementById('cycle-select');
    const subjectSelect = document.getElementById('subject-select');

    let reportData;

    if (type === 'final') {
        reportData = {
            type: type,
            cycle: cycleSelect.value,
            subject: subjectSelect.value,
            data: unidadData
        };
    } else {
        const unitNumber = type;
        reportData = {
            type: `unidad${unitNumber}`,
            cycle: cycleSelect.value,
            subject: subjectSelect.value,
            data: unidadData[`unidad${unitNumber}`]
        };
    }

    fetch('/login/moduloDocentes/send_report', {
        method: 'POST',
        body: JSON.stringify(reportData),
        headers: { 'Content-Type': 'application/json' }
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                Swal.fire({
                    icon: 'success',
                    title: 'Éxito',
                    text: 'Reporte enviado correctamente'
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Error al enviar el reporte: ' + (data.message || 'Error desconocido')
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al enviar el reporte'
            });
        });
}


function getPrediction(id) {
    const studentUnidad1 = unidadData.unidad1 ? unidadData.unidad1.find(s => s.Id.toString() === id) : null;
    const studentUnidad2 = unidadData.unidad2 ? unidadData.unidad2.find(s => s.Id.toString() === id) : null;
    const studentUnidad3 = unidadData.unidad3 ? unidadData.unidad3.find(s => s.Id.toString() === id) : null;

    let mensaje = '';
    let notaNecesaria1 = 0;
    let notaNecesaria2 = 0;
    let icon = 'info';

    if (studentUnidad1 && studentUnidad2 && studentUnidad3) {
        const sumaTotal = studentUnidad1.Promedio + studentUnidad2.Promedio + studentUnidad3.Promedio;
        if (sumaTotal >= 21) {
            mensaje = 'Aprobado';
            icon = 'success';
        } else {
            mensaje = 'Supletorio';
            icon = 'error';
        }
    }
    else if (studentUnidad2 && studentUnidad3) {
        const sumaActual = studentUnidad2.Promedio + studentUnidad3.Promedio;
        notaNecesaria1 = 21 - sumaActual;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 1 para aprobar`;
            icon = 'info';
        }
    }
    else if (studentUnidad1 && studentUnidad3) {
        const sumaActual = studentUnidad1.Promedio + studentUnidad3.Promedio;
        notaNecesaria1 = 21 - sumaActual;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 2 para aprobar`;
            icon = 'info';
        }
    }
    else if (studentUnidad1 && studentUnidad2) {
        const sumaActual = studentUnidad1.Promedio + studentUnidad2.Promedio;
        notaNecesaria1 = 21 - sumaActual;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 3 para aprobar`;
            icon = 'info';
        }
    }
    else if (studentUnidad3) {
        notaNecesaria1 = (21 - studentUnidad3.Promedio) / 2;
        notaNecesaria2 = notaNecesaria1;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 1 y ${notaNecesaria2.toFixed(2)} en la Unidad 2 para aprobar`;
            icon = 'info';
        }
    }
    else if (studentUnidad2) {
        notaNecesaria1 = (21 - studentUnidad2.Promedio) / 2;
        notaNecesaria2 = notaNecesaria1;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 1 y ${notaNecesaria2.toFixed(2)} en la Unidad 3 para aprobar`;
            icon = 'info';
        }
    }
    else if (studentUnidad1) {
        notaNecesaria1 = (21 - studentUnidad1.Promedio) / 2;
        notaNecesaria2 = notaNecesaria1;
        if (notaNecesaria1 > 10) {
            mensaje = 'Supletorio';
            icon = 'error';
        } else {
            mensaje = `Necesita sacar ${notaNecesaria1.toFixed(2)} en la Unidad 2 y ${notaNecesaria2.toFixed(2)} en la Unidad 3 para aprobar`;
            icon = 'info';
        }
    }
    else {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Se necesitan datos de al menos una unidad adicional (Unidad 2 o Unidad 3)'
        });
        return;
    }

    Swal.fire({
        icon: icon,
        title: 'Proyección',
        text: mensaje
    });
}

function downloadReport(reportId) {
    window.location.href = `/download_report/${reportId}`;
}

function viewReport(reportId) {
    window.open(`/view_report/${reportId}`, '_blank');
}

function updateStudent(matricula) {
    alert(`actualizan el estudiante por medio de su id ${matricula}`);
}
