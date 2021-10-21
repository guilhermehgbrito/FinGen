// Call the dataTables jQuery plugin 
$(document).ready(function() {
  $('#atividades-table').DataTable({
    "scrollY": "300px",
    "scrollX": false,
    "scrollCollapse": true,
    "language": {
      "url": "https://cdn.datatables.net/plug-ins/1.11.3/i18n/pt_br.json"
    }
  });
});
