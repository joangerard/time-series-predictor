var trs = document.getElementById('completedJob-table').children[1].children
var arr = []

for (var i = 0; i < trs.length; i++) {
    arr.push(+trs[i].children[3].textContent.split(' ')[0])
}

arr
