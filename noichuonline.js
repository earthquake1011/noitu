function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}


function getResult(text)
{
    let url = 'http://localhost:6969?text=' + text;
    return httpGet(url);
}

setInterval(function(){
    if ($('.swal-overlay.swal-overlay--show-modal .swal-button--confirm').length) {
        $('.swal-overlay.swal-overlay--show-modal .swal-button--confirm').click()
    }
},1000)


setInterval(function(){
    if ($('.swal-overlay.swal-overlay--show-modal .swal-button--confirm').length) {
        $('.swal-overlay.swal-overlay--show-modal .swal-button--confirm').click()
    }
},1000)

setInterval(function(){
    if ($('.swal-overlay.swal-overlay--show-modal .swal-button--confirm').length ==0) {
        if ($('#group-text input').attr('disabled') == undefined) {
            $('#group-text input').val(
                getResult($('#head').text())
            )
            $('#group-text input')[0].focus();
            
            var input = document.querySelector("#group-text input");
            var ev = document.createEvent('Event');
            ev.initEvent('keypress');
            ev.which = ev.keyCode = 13;
            input.dispatchEvent(ev);


        }
    }
},1000)

$('#head').text()
