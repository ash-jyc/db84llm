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
                render: function(data) {
                    return `${data.aff_school} ${data.aff_code}`;
                }
            },
            {
                data: null,
                render: function(data) {
                    return `${data.neg_school} ${data.neg_code}`;
                }
            },
            {
                data: 'aff_doc',
                render: function(data) {
                    return `<a href="https://api.opencaselist.com/v1/download?path=${data}" class="table-icon" target="_blank"><i class="fas fa-file-alt" style="font-size:20px;"></i></a>`;
                }
            },
            {
                data: 'neg_doc',
                render: function(data) {
                    return `<a href="https://api.opencaselist.com/v1/download?path=${data}" class="table-icon" target="_blank"><i class="fas fa-file-alt" style="font-size:20px;"></i></a>`;
                }
            },
            {
                data: 'yt_link',
                render: function(data) {
                    // only show icon if there is a link
                    if (data) {
                        return `<a href="${data}" class="table-icon yt-icon" target="_blank"><i class="fab fa-youtube" style="font-size:20px;"></i></a>`;
                    } else {
                        return '';
                    }
                }
            }
        ],
        paging: true,
        pageLength: 25,
        searching: true,
        ordering: true,
        order: [[0, 'asc']]
    });

    function applySearch() {
        const tournamentName = $('#searchTournament').val().toLowerCase();
        const roundName = $('#searchRound').val().toLowerCase();
        const affTeam = $('#searchAffTeam').val().toLowerCase();
        const negTeam = $('#searchNegTeam').val().toLowerCase();

        table.column(0).search(tournamentName);
        table.column(1).search(roundName);
        table.column(2).search(affTeam);
        table.column(3).search(negTeam);
        table.draw();
    }

    $('#searchTournament, #searchRound, #searchAffTeam, #searchNegTeam').on('input', function() {
        applySearch();
    });

    $('#clearButton').on('click', function() {
        $('#searchTournament').val('');
        $('#searchRound').val('');
        $('#searchAffTeam').val('');
        $('#searchNegTeam').val('');
        applySearch();
    });

});
