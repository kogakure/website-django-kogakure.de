$(document).ready(function(){
    main();
});

function main() {
    var nav  = $('ul.nav');
    var path = window.location.pathname.split('/').slice(1,-1);
    function act(p) {
        nav.not(nav.find('li.aktiv').parent()).find('li>a[@href="/'+p+'"]').addClass('aktiv');
    }
    if (path.length) {
        for (; path.length; path.pop()) {
            act(path.join('/')+'/');
        }
    } else {
        act('');
    }
}