$(document).ready(function() {
    const table = $('#caselist-table').DataTable({
        ajax: {
            url: '/api/caselist',  // Adjust this URL to your API endpoint
            dataSrc: ''
        },
        columns: [
            { data: 'tournament_name' },
            { data: 'round_name' },
            {
                data: null,
                render: function(data, type, row) {
                    return `${row.aff_school} ${row.aff_code}`;
                }
            },
            {
                data: null,
                render: function(data, type, row) {
                    return `${row.neg_school} ${row.neg_code}`;
                }
            },
            {
                data: 'aff_doc',
                render: function(data) {
                    return `<a href="https://api.opencaselist.com/v1/download?path=${data} class="table-icon" target="_blank"><i class="fas fa-file-alt" style="font-size:20px;"></i></a>`;
                }
            },
            {
                data: 'neg_doc',
                render: function(data) {
                    return `<a href="https://api.opencaselist.com/v1/download?path=${data} class="table-icon" target="_blank"><i class="fas fa-file-alt" style="font-size:20px;"></i></a>`;
                }
            },
            {
                data: 'yt_link',
                render: function(data) {
                    return `<a href="${data}" target="_blank"><i class="fab fa-youtube" style="font-size:20px;"></i></a>`;
                }
            }
        ],
        paging: true,
        pageLength: 25,
        searching: true,
        ordering: true,
        order: [[0, 'asc']] // Default sorting by first column
    });

    // Custom search functionality
    $('#searchInput').on('input', function() {
        const searchBy = $('#searchBy').val();
        const searchValue = this.value.toLowerCase();

        if (searchBy === 'all') {
            // Search across all columns
            table.search(searchValue, true, false).draw();
        } else {
            // Search only the specified column
            const columnIndex = $('#searchBy').find('option:selected').data('column');
            table.column(columnIndex).search(searchValue, true, false).draw();
        }
    });

    $('#searchBy').on('change', function() {
        $('#searchInput').trigger('input');
    });
});
