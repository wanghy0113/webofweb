var infowindow = d3.select(".tooltip")
		.style("position","absolute")
		.style("opacity",0);

d3.select("#tooltip_table")
		.attr("width",info_window_dimension.width)
		.attr("top","0px")
		.attr("left","0px");