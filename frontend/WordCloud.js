!function(){
    var WordCloud = {};

    WordCloud.drawWordCloud = function (word_count){
        //var d3 = d3version4_13;
        words = Object.keys(word_count);
        var svg_location = "#forCloud";
        d3.select(svg_location).selectAll("*").remove();
        var node  = d3.select(svg_location).node();
        var rectBoxInfo = node.getBoundingClientRect();
        var width = rectBoxInfo.width; //$(document).width();
        var height = rectBoxInfo.height; //$(document).height();

        //var fill = d3.scale.category20();
        //var fill = d3.scaleOrdinal(d3.schemeCategory20);
        var fill = function (i) {
            if(i%3 == 0) {
                return donutColors.negative;
            } else if(i%3 == 1) {
                return donutColors.neutral;
            } else {
                return donutColors.positive;
            }
        };

        var word_entries = d3.entries(word_count);

        var xScale = d3.scale.linear()
            .domain([0, d3.max(word_entries, function(d) {
                return d.value.freq;
            })
            ])
            .range([10,100]);

        d3.layout.cloud().size([width, height])
            .timeInterval(20)
            .words(word_entries)
            .fontSize(function(d) { return xScale(+d.value.freq); })
            .text(function(d) { return d.key; })
            .rotate(function() { return ~~(Math.random() * 2) * 90; })
            .font("Impact")
            .on("end", draw)
            .start();

        function draw(words) {
            d3.select(svg_location).append("svg")
                .attr("width", width)
                .attr("height", height)
            .append("g")
                .attr("transform", "translate(" + [width >> 1, height >> 1] + ")")
            .selectAll("text")
                .data(words)
            .enter().append("text")
                .style("font-size", function(d) { return xScale(d.value.freq) + "px"; })
                .style("font-family", "Impact")
                .style("fill", function(d, i) { return fill(d.value.sent); })
                .attr("text-anchor", "middle")
                .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function(d) { return d.key; });
        }

        d3.layout.cloud().stop();
        
    }

    this.WordCloud = WordCloud;
}();