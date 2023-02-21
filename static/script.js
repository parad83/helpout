function copyLink(id) {
    var copyText = document.getElementById(id).innerHTML;
    alert(copyText);
    alert(typeof copyText);

    copyText.select();
    copyText.setSelectionRange(0, 99999);
  
    navigator.clipboard.writeText(copyText);
}

