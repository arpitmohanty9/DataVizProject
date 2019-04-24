!function(){
    var LineChart = {};

    LineChart.createLine = function(year_data) {
        console.log(year_data);
        var d3 = d3version4_10;
        // 2. Use the margin convention practice 
        var svg_location = "#forLineChart";
        d3.select(svg_location).selectAll("*").remove();
        var node  = d3.select(svg_location).node();
        var rectBoxInfo = node.getBoundingClientRect();
        var width = rectBoxInfo.width-50; //$(document).width();
        var height = rectBoxInfo.height-50; //$(document).height();
        var margin = {top: 20, right: 20, bottom: 20, left: 30}
        //, width = window.innerWidth - margin.left - margin.right // Use the window's width 
        //, height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

        // The number of datapoints
        var n = 10;



        // 5. X scale will use the index of our data
        var xScale = d3.scaleLinear()
        .domain([2005, 2014]) // input
        // .domain([0, n-1]) // input
        .range([0, width]); // output

        // 6. Y scale will use the randomly generate number 
        var yScale = d3.scaleLinear()
        .domain([0, d3.max(Object.values(year_data))]) // input
        .range([height, 0]); // output 

        // 7. d3's line generator
        var line = d3.line()
        .x(function(d, i) { return xScale(i+2005); }) // set the x values for the line generator
        .y(function(d) { return yScale(d.y); }) // set the y values for the line generator 
        .curve(d3.curveMonotoneX) // apply smoothing to the line

        // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
        var dataset = d3.range(n).map(function(d,i) {
            console.log(i);
            var year = 2005 + i;
            if (year_data[year]) {
                return {"y": year_data[year]}
            } else {
                return {"y": 0}
            }
        });
        console.log("Dataset Test ")
        console.log(dataset)

        // 1. Add the SVG to the page and employ #2
        var svg = d3.select(svg_location).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // 3. Call the x axis in a group tag
        svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale).tickFormat(d3.format("d"))); // Create an axis component with d3.axisBottom

        // 4. Call the y axis in a group tag
        svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

        // 9. Append the path, bind the data, and call the line generator 
        svg.append("path")
        .datum(dataset) // 10. Binds data to the line 
        .attr("class", "line") // Assign a class for styling 
        .attr("d", line); // 11. Calls the line generator

        // Define the div for the tooltip
        var div = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        // 12. Appends a circle for each datapoint 
        svg.selectAll(".dot")
        .data(dataset)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot") // Assign a class for styling
        .attr("cx", function(d, i) { return xScale(i+2005) })
        .attr("cy", function(d) { return yScale(d.y) })
        .attr("r", 5)
        .on("mouseover", function(d, i) {
            console.log(d.y)
            $(this).attr('class', 'focus');
            // Define the div for the tooltip
            div.transition()
                .duration(200)
                .style("opacity", .9);
            // div.html("Total sales figure in " + (i+2005) + "<br>" + d.y)
            div.html("Total sales <br>" + d.y)
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");

        })
        .on("mouseout", function() {
            $(this).attr('class', 'dot')
            div.transition()
                .duration(500)
                .style("opacity", 0);
        });
    };

    this.LineChart = LineChart;
}();