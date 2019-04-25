!function () {
    var pieChart = {};

    pieChart.makePie = function (sentiment_data, index) {
        console.log(sentiment_data);
        var svg_location = "#forSentiment";
        var salesData = [
            {label: "Negetive", color: "#db4437"},
            {label: "Neutral", color: "#f4b400"},
            {label: "Positive", color: "#4285f4"}
        ];
        if (index === 0) {
            var node = d3.select(svg_location).node();
            var rectBoxInfo = node.getBoundingClientRect();
            var width = rectBoxInfo.width; //$(document).width();
            var height = rectBoxInfo.height; //$(document).height();

            var svg = d3.select(svg_location).append("svg").attr("width", width).attr("height", height);
            // var svg = node.append("svg").attr("width",width).attr("height",height);

            svg.append("g").attr("id", "salesDonut");
            // svg.append("g").attr("id","quotesDonut");


            // Legend
            var legendG = svg.selectAll(".legend") // note appending it to mySvg and not svg to make positioning easier
                .data(salesData)
                .enter().append("g")
                .attr("transform", function (d, i) {
                    return "translate(" + (width - 110) + "," + (i * 15 + 20) + ")"; // place each legend on the right and bump each one down 15 pixels
                })
                .attr("class", "legend");

            legendG.append("rect") // make a matching color rect
                .attr("width", 10)
                .attr("height", 10)
                .attr("fill", function (d) {
                    return d.color;
                });

            legendG.append("text") // add the text
                .text(function (d) {
                    return d.label;
                })
                .style("font-size", 12)
                .attr("y", 10)
                .attr("x", 11);



            // console.log(data);
            $(svg_location).hide();
            Donut3D.draw("salesDonut", randomData(), 200, 200, 150, 120, 30, 0.4);
        } else {
            $(svg_location).show();
            Donut3D.transition("salesDonut", createData(), 150, 120, 30, 0.4);
        }

        function randomData() {
            return salesData.map(function (d) {
                return {label: d.label, value: 1, color: d.color};
            });
        }

        function createData() {
            return salesData.map(function (d) {
                return {label: d.label, value: sentiment_data[d.label], color: d.color};
            });
        }
    }

    this.pieChart = pieChart;
}();