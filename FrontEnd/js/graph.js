/**
 * Created by HongyiWang on 11/28/14.
 */
function myGraph(vis) {



    // Add and remove elements on the graph object
    this.addNode = function (node) {
        nodes.push(node);
        console.log("node id: "+node.id);
        update();
    }

    this.removeNode = function (node) {
        var i = 0;
        var n = findNode(node.id);
        while (i < links.length) {
            if ((links[i]['source'] === n)||(links[i]['target'] == n)) links.splice(i,1);
            else i++;
        }
        var index = findNodeIndex(id);
        if(index !== undefined) {
            nodes.splice(index, 1);
            update();
        }
    }

    this.addLink = function (sourceId, targetId) {
        var sourceNode = findNode(sourceId);
        var targetNode = findNode(targetId);

        if((sourceNode !== undefined) && (targetNode !== undefined)) {
            links.push({"source": sourceNode, "target": targetNode});
            update();
        }
    }

    var findNode = function (id) {
        for (var i=0; i < nodes.length; i++) {
            if (nodes[i].id === id)
                return nodes[i]
        };
    }

    var findNodeIndex = function (id) {
        for (var i=0; i < nodes.length; i++) {
            if (nodes[i].id === id)
                return i
        };
    }

    // set up the D3 visualisation in the specified element
    var w = force_dimension.width,
        h = force_dimension.height,
        r = circle_base_radius;
    var force = d3.layout.force()
        .gravity(.05)
        .distance(100)
        .charge(-100)
        .size([force_dimension.width, force_dimension.height]);

    var nodes = force.nodes(),
        links = force.links();

    var p = d3.scale.category20();

    var update = function () {

        var link = vis.selectAll("line.link")
            .data(links, function(d) { return d.source.id + "-" + d.target.id; });

        link.enter().insert("line")
            .attr("class", "link")
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; })
            .attr("stroke-width", 1)
            .attr("stroke", "gray");

        link.exit().remove();

        var node = vis.selectAll("g.node")
            .data(nodes, function(d) { return d.id;});

        var nodeEnter = node.enter().append("g")
            .attr("class", "node")
            .call(force.drag);

        nodeEnter.append("circle")
            .attr("r", circle_base_radius)
            .attr("fill", function (d) {
                if(!d.node_parent) return "red";
                var type = d.node_type;
                if(type.indexOf("html")!=-1) return p(1);
                if(type.indexOf("pdf")!=-1) return p(2);
                if(type.indexOf("csv")!=-1) return p(3);
                return "steelblue";

            });

        //nodeEnter.append("text")
        //    .attr("class", "nodetext")
        //    .attr("dx", 12)
        //    .attr("dy", ".35em")
        //    .text(function(d) {return d.id});

        node.exit().remove();

        force.on("tick", function() {

            //node.attr("cx", function(d) { return d.x = Math.max(r, Math.min(w - r, d.x)); })
            //    .attr("cy", function(d) { return d.y = Math.max(r, Math.min(h - r, d.y)); });

            link.attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; });

            node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

        });

        // Restart the force layout.
        force.start();
    }

    // Make it all go
    update();
}