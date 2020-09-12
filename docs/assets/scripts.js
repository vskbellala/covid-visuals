    // Set options
    marked.setOptions({
        headerIds: false
    });

    //Master Path for MD content
    let mpath = 'https://bellala.org/covid-visuals/content/';

    //Function for reading MD file
    function readFile(file, out) {
        var http = new XMLHttpRequest();
        http.open('get', mpath + file);
        http.onreadystatechange = function() {
            document.getElementById(out).innerHTML = marked(http.responseText); //conversion to html using marked.js + place html code into div
        };
        http.send();
    }

    // Functions + Helpers for dynamic Timeline construction

    const parseHTMLString = (() => {
        const parser = new DOMParser();
        return str => parser.parseFromString(str, "text/html");
    })(); // required for getting h6 headers from marked text

    //Function for reading MD file for timeline
    function readTime(file, out) {
        var http = new XMLHttpRequest();
        http.open('get', mpath + file);
        http.onreadystatechange = function() {
            var mark = marked(http.responseText);
            document.getElementById(out).innerHTML = mark; //conversion to html using marked.js + place html code into div
            var mhtml = parseHTMLString(mark);
            document.getElementById(out).setAttribute("date-is", mhtml.querySelector("h6").innerHTML);
            // set 'date-is' attribute using the inner html of the h6 header
            // h6 headers are set to display:none; in css
        };
        http.send();
    }



    // for easier plotly embeds
    $.fn.embed.settings.sources = {
        plotly: {
            name: 'plotly',
            type: 'html',
            icon: 'play',
            url: '../plots/{id}.html',
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

    /*
    Deprecated timeline script
    
    function addTime(entries) {
        let time = document.getElementById("timeline");
        if (time != null) {
            time.innerHTML = "";
            for (let i = 0; i < entries.length; i++) {
                let mhtml = parseHTMLString(entries[i].html);
                time.innerHTML += "<div class='timeline-item' date-is='"+mhtml.querySelector("h6").innerHTML+"''>"+entries[i].html+"</div>";
            }
        }
    }

    function makeTimeline(files,path) {
        let entries = [];
        files.reverse();
        for (let f = 0; f < files.length; f++) {
            let client = new XMLHttpRequest();
            client.open('GET', mpath+path+files[f]);
            client.send();
            client.onreadystatechange = function() {
                if (client.readyState != 4) return;
                let html = marked(client.responseText);
                entries.push({ html: html, url: client.responseURL });
                addTime(entries);
            }
        }
    }
    */