/**
 * Created by HongyiWang on 11/29/14.
 */
function choose_max_node(num)
{
    d3.select("#max-node").text("Max:"+num);
    max_node = num;
}

function choose_max_depth(num)
{
    d3.select("#max-depth").text("Depth:"+num);
    max_depth = num;
}