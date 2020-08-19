    // Set options
    marked.setOptions({
        headerIds: false
    });

    //Function for reading MD file
    function readFile(file, out) {
        var http = new XMLHttpRequest();
        http.open('get', file);
        http.onreadystatechange = function() {
            document.getElementById(out).innerHTML = marked(http.responseText); //.replace(/\n/g, '<br>'));
        };
        http.send();
    }
    const parseHTMLString = (() => {
        const parser = new DOMParser();
        return str => parser.parseFromString(str, "text/html");
    })();
    //Function for reading MD file for timeline
    function readTime(fil, out) {
        var http = new XMLHttpRequest();
        http.open('get', fil);
        http.onreadystatechange = function() {
            var mark = marked(http.responseText);
            document.getElementById(out).innerHTML = mark; //.replace(/\n/g, '<br>'));
            var mhtml = parseHTMLString(mark);
            document.getElementById(out).setAttribute("date-is", mhtml.querySelector("H6").innerHTML);
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