/**
 * Created by HongyiWang on 11/27/14.
 */


var resize_rate = 1.0;
var main_dimension = {
    width:900,
    height:600
};

var center_point = {
    cx:450,
    cy:300
}

var circle_base_radius = 30;
var circle_radius_decrease_rate = 0.75;
main_dimension.width = main_dimension.width * resize_rate;
main_dimension.height = main_dimension.height * resize_rate;
circle_base_radius = circle_base_radius * resize_rate;

