    // Set options
    marked.setOptions({
        headerIds: false
    });

    //Function for reading MD file
    function readFile(file, out, x) {
        var http = new XMLHttpRequest();
        http.open('get', file);
        http.onreadystatechange = function() {
            var mark = marked(file);
            document.getElementById(out).innerHTML = mark; //.replace(/\n/g, '<br>'));
            var date = document.getElementsByTagName('h6')[x].innerHTML;
            document.getElementById(out).setAttribute("date-is", date);
        };
        http.send();
    }
/*
    $.fn.embed.settings.sources = {
        plotly: {
            name: 'plotly',
            type: 'html',
            icon: 'play',
            url: '../../plots/{id}.html',
            placeholder : '../../content/images/me.PNG',
            parameters: function(settings) {
                return {
                    autohide: !settings.showUI,
                    autoplay: settings.autoplay,
                    color: settings.colors || undefined,
                    hq: settings.hd,
                    jsapi: settings.api,
                    modestbranding: 1,

                };
            }
        },
    };

    */