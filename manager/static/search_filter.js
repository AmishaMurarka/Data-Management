// JavaScript source code

function getIndex(row) {
    index = row.rowIndex;
    var data = '{{ excel_data }}';

}

function myFunction() {
    var input, filter, table, tr, td, i;
    var x = parseInt(document.getElementById("filter").value);
    if (x == 99) {
        x = 0;
    }

    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("info_table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[x];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
