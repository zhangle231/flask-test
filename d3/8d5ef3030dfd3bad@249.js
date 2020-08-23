// https://observablehq.com/@d3/histogram@249
export default function define(runtime, observer) {
  const main = runtime.module();
  const fileAttachments = new Map([["unemployment-x.csv",new URL("./files/8a6057f29caa4e010854bfc31984511e074ff9042ec2a99f30924984821414fbaeb75e59654e9303db359dfa0c1052534691dac86017c4c2f992d23b874f9b6e",import.meta.url)]]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));

  main.variable(observer("data")).define("data",["d3"], function(d3){
	  return (
	    d3.json("http://127.0.0.1:8000/files/a.txt", function(error, text) {
	      return text;
            })
	  )
  	}
  );

  main.variable(observer("chart")).define("chart", ["d3","width","height","bins","x","y","xAxis","yAxis","data"], 
	                                         function(d3,width,height,bins,x,y,xAxis,yAxis,data) {
  const svg = d3.create("svg").attr("width",1800)
      .attr("viewBox", [0, 0, width, height]);

  var my_datas = [];
  for (var j = 0; j < 24; j++) {
    var my_data = [];
    for (var i = 0; i < 24 * 4; i++) {
      my_data.push({data:10, running: (Math.floor((Math.random()*10)+1)) % 2});
    }
    my_datas.push(my_data)
  }

  my_datas = data;
  for (var i = 0; i < 24; i++) {
    my_data = my_datas[i];
    svg.append("g")
	.attr("fill", "steelblue")
	.selectAll("circle")
	.data(my_data, function(d) { return d; })
	.join("circle")
	.attr("cy", 50 * i + 50)
	.attr("cx", function(d,i) {return i * 30 + 30 })
	.attr("r", function(d) {return d.data; })
	.transition()
	.on("start", function repeat() {
           d3.active(this)
            .style("fill", "black")
          .transition()
            .style("fill", function(d) {
		if (d.running == 1) {
			return "red";
		}
		return "black";
          })
         // .transition()
         //   .duration(200)
         //   .delay(200)
         //   .on("start", repeat);
        });
  }
  svg.append('g')
  .selectAll("text")
  .data(my_data, function(d) { return d.data; })
  .join("text")
  .text(function(d,i) {return i;} )
  .attr("x", function(d,i) {return i * 30 + 25})
  .attr('y',25)

  /*
  svg.append("g")
      .attr("fill", "steelblue")
    .selectAll("rect")
    .data(bins)
    .join("rect")
      .attr("x", d => x(d.x0) + 1)
      .attr("width", d => Math.max(0, x(d.x1) - x(d.x0) - 1))
      .attr("y", d => y(d.length))
      .attr("height", d => y(0) - y(d.length));

  svg.append("g")
      .call(xAxis);
  
  svg.append("g")
      .call(yAxis);
  
  */
  return svg.node();
}
);


  //main.variable(observer("data")).define("data", ["d3","FileAttachment"], async function(d3,FileAttachment){return(
  //main.variable().define("data", ["d3","FileAttachment"], async function(d3,FileAttachment){return(
  //Object.assign(d3.csvParse(await FileAttachment("unemployment-x.csv").text(), ({rate}) => +rate), {x: "Unemployment (%)", y: "Counties"})
  //)});



  //main.variable(observer("bins")).define("bins", ["d3","x","data"], function(d3,x,data){return(
  main.variable().define("bins", ["d3","x","data"], function(d3,x,data){return(
  d3.histogram()
    .domain(x.domain())
    .thresholds(x.ticks(40))
  (data)
)});
  main.variable().define("x", ["d3","data","margin","width"], function(d3,data,margin,width){return(
d3.scaleLinear()
    .domain(d3.extent(data)).nice()
    .range([margin.left, width - margin.right])
)});
  main.variable().define("y", ["d3","bins","height","margin"], function(d3,bins,height,margin){return(
d3.scaleLinear()
    .domain([0, d3.max(bins, d => d.length)]).nice()
    .range([height - margin.bottom, margin.top])
)});
  main.variable().define("xAxis", ["height","margin","d3","x","width","data"], function(height,margin,d3,x,width,data){return(
g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(width / 80 ).tickSizeOuter(0))
    .call(g => g.append("text")
        .attr("x", width - margin.right)
        .attr("y", -4)
        .attr("fill", "currentColor")
        .attr("font-weight", "bold")
        .attr("text-anchor", "end")
        .text(data.x))
)});
  main.variable().define("yAxis", ["margin","d3","y","height","data"], function(margin,d3,y,height,data){return(
g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(height / 40))
    .call(g => g.select(".domain").remove())
    .call(g => g.select(".tick:last-of-type text").clone()
        .attr("x", 4)
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text(data.y))
)});
  main.variable(observer("height")).define("height", function(){return( 1300)});
  main.variable(observer("width")).define("width", function(){return( 2900)});
  main.variable(observer("margin")).define("margin", function(){return( {top: 20, right: 20, bottom: 30, left: 40})});
  main.variable(observer("d3")).define("d3", ["require"], function(require){return(
require("d3@5")
)});
  return main;
}
