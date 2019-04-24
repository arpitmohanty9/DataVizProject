!function(){
    var BubbleChart = {};

    var d3 = d3version4_10;

    function createChart(dataset) {
        console.log(dataset);
    }

    function createBubbleChart(dataset){
        dataset = {"children":dataset};
        console.log(dataset);

        var diameter = 600;
        var color = d3.scaleOrdinal(d3.schemeCategory20);

        var bubble = d3.pack(dataset)
            .size([diameter, diameter])
            .padding(1.5);

        var svg = d3.select("#forBubble")
            .append("svg")
            .attr("width", diameter)
            .attr("height", diameter)
            .attr("class", "bubble");

        var nodes = d3.hierarchy(dataset)
            .sum(function(d) { return d.Count; });

        var node = svg.selectAll(".node")
            .data(bubble(nodes).descendants())
            .enter()
            .filter(function(d){
                return  !d.children
            })
            .append("g")
            .attr("class", "node")
            .attr("id", function(d) {
                return d.data.Name;
            })
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            })
            .on("click", function(d) {
                console.log("Mouse Clicked " + d.data.Name);

                // Create the word cloud using brand data
                $.getJSON("../data/wordcloud_all.json",function(json) {
                    console.log(d.data.Name); // this will show the info it in firebug console
                    console.log(json[d.data.Name]); // this will show the info it in firebug console
                    WordCloud.drawWordCloud(json[d.data.Name]);
                });

                // Create the line chart using brand data
                $.getJSON("../data/yearlyReview.json",function(json) {
                    console.log(d.data.Name); // this will show the info it in firebug console
                    console.log(json[d.data.Name]); // this will show the info it in firebug console
                    LineChart.createLine(json[d.data.Name]);
                });
            })
        ;

        node.append("title")
            .text(function(d) {
                return d.data.Name + ":" + d.data.Count;
            });

        node.append("circle")
            .attr("r", function(d) {
                return d.r;
            })
            .style("fill", function(d,i) {
                return color(i);
            });

        node.append("text")
            .attr("dy", ".2em")
            .style("text-anchor", "middle")
            .text(function(d) {
                return d.data.Name.substring(0, d.r / 3);
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", function(d){
                return d.r/5;
            })
            .attr("fill", "white");

        node.append("text")
            .attr("dy", "1.3em")
            .style("text-anchor", "middle")
            .text(function(d) {
                return d.data.Count;
            })
            .attr("font-family",  "Gill Sans", "Gill Sans MT")
            .attr("font-size", function(d){
                return d.r/5;
            })
            .attr("fill", "white");

        d3.select(self.frameElement)
            .style("height", diameter + "px");
    }

    var config = {
        download: true,
        header: true,
        complete: function(results, file) {
            allData = results;
            createBubbleChart(results.data);
        }
    };

    BubbleChart.loadChart = function () {
        Papa.parse('../data/Topbrand.csv',config);
    };
    this.BubbleChart = BubbleChart;
}();