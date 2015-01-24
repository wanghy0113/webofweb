function pop_up_info_window(d){
	infowindow.transition()
		.duration(200)
		.style("display","block")
		.style("opacity",0.9);

	var left_position = parseInt(d["x"]);
	var top_position = parseInt(d["y"]);

	if(parseInt(d["x"])>force_dimension.width/2)
	{
		infowindow.style("right",force_dimension.width-left_position+10+"px");
		infowindow.style("top",top_position+10+"px");
		infowindow.style("left","");

	}else{
		infowindow.style("left", left_position+10+"px");
		infowindow.style("top",top_position+10+"px");
		infowindow.style("right","");
	}
	
	d3.select("#node_url_value").text(": "+d["node_url"]);
	//d3.select("#matter_number").text("Matter No. "+d["doc_matter_no"]);
	d3.select("#node_referer_value").text(": "+d["node_parent"]);
	//d3.select("#group").text("Group : "+d["group"]);
	d3.select("#node_type_value").text(": "+d["node_type"]);
	//d3.select("#doc_create_date").text(d["doc_create_date"]);
}

function fade_out_info_window(d){
	infowindow.transition()
		.delay(200)
		.duration(200)
		.style("opacity",0)
		.style("display","none");
}
