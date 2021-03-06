// получение json через Django API
var datas = 'http://127.0.0.1:8000/api/sessions/?format=json'

// приведение к формату HeatMap
var parser = function(data) {
    var stats = {}
    for (var d in data) {
        stats[data[d].in_seconds] = data[d].total;
    }
    return stats;
}

var cal = new CalHeatMap();
cal.init({
    data: datas,
    afterLoadData: parser,

    //domain: "month",
    domain: "week",
    subDomain: "day",
    range: 30,
    cellSize: 25,
    cellPadding: 3,
    cellRadius: 5,
    label: {position: "top"},
    domainLabelFormat: "",
    subDomainTextFormat: "%d",      // убрать нолик
    
    // с базовым цветом пока непонятно
    legendColors: {
        //min: "#999CDF",
        min: "#ededed",
        max: "#070B56",
        //base: "#ededed",
        //empty: "#ededed"
    },

    tooltip: true,
    
    start: new Date(2021, 9, 15),
    //displayLegend: false,
    legendCellSize: 30,
    legend: [1, 2, 3, 4],
});