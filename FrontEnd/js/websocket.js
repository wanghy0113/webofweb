/**
 * Created by HongyiWang on 11/28/14.
 */
if ("WebSocket" in window)
{
    // Let us open a web socket
    var ws = new WebSocket("ws://54.148.253.239:61616/echo");
    //var ws = new WebSocket("ws://localhost:9988/echo");
    function startWeave() {
        var url = 'http://'+d3.select("#start_url").property("value");
        console.log("start url: "+url);
        ws.close();
        //ws = new WebSocket("ws://localhost:9988/echo");
        ws = new WebSocket("ws://54.148.253.239:61616/echo");
        //remove previous svg
        d3.select("#svg-component").remove();

        var w = $("#main-area").innerWidth(),
            h = $("#main-area").innerHeight();
        console.log("w: "+w+"  h: "+h);

        //add new svg
        var vis = d3.select("#main-area").append("svg")
            .attr("width", w)
            .attr("height", h)
            .attr("id", "svg-component");
        var graph = new myGraph(vis);
        var num = 0;
        var url_hash = {};
        ws.onopen = function()
        {
            console.log("socket opened!");
            var weave_signal = {"url":url, "command":"start", "max_node":max_node, "max_depth":max_depth};
            ws.send(JSON.stringify(weave_signal));
            console.log(JSON.stringify(weave_signal));
        }
        ws.onmessage = function (evt)
        {
            var received_msg = evt.data+"";
            var node = JSON.parse(received_msg);
            var depth = node.node_depth;
            if(!url_hash[node["node_url"]])
            {
                num++;
                node.id = "node"+num;
                url_hash[node["node_url"]] = node;
                graph.addNode(node);
                var p = url_hash[node["node_parent"]];
                if(p) graph.addLink(p["id"], "node"+num);
            }
            else
            {
                var p = url_hash[node["node_parent"]];
                graph.addLink(p["id"], url_hash[node["node_url"]].id);
            }
        };
        ws.onclose = function()
        {
            console.log("socket closed!");
        };

    }
}
else
{
    // The browser doesn't support WebSocket
    alert("WebSocket NOT supported by your Browser!");
}