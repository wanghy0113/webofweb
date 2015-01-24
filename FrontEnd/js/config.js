/**
 * Created by HongyiWang on 11/27/14.
 */


var resize_rate = 1.0;
var force_dimension = {
    width:1000,
    height:800
};

var circle_base_radius = 10;
var default_max_node = 100;
var default_max_depth = 10;
var max_node = default_max_node;
var max_depth = default_max_depth;
force_dimension.width = force_dimension.width * resize_rate;
force_dimension.height = force_dimension.height * resize_rate;
circle_base_radius = circle_base_radius * resize_rate;


//-------- info window
var info_window_dimension = {
	width:160,
	x_offset:40,
	y_offset:8,
}