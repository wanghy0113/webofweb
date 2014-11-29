/**
 * Created by HongyiWang on 11/27/14.
 */


var resize_rate = 1.0;
var force_dimension = {
    width:1000,
    height:1000
};

var circle_base_radius = 10;
force_dimension.width = force_dimension.width * resize_rate;
force_dimension.height = force_dimension.height * resize_rate;
circle_base_radius = circle_base_radius * resize_rate;


