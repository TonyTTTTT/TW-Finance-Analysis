import React from "react";
// import * as echarts from "echarts";
import axios from "axios";
import ReactEcharts from "echarts-for-react"

class HomePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            TAIEX: {},
            fund: {}
        };
        this.chart = null;
    }

    componentDidMount() {
        axios.get('/api/get-TAIEX').then(
            response => {
                this.setState({TAIEX: response.data})
                console.log('response from get-TAIEX:');
                console.log(response);
                console.log("this.state.TAIEX:");
                console.log(this.state.TAIEX);
            }
        );

        axios.get('/api/get-Foreign-Fund').then(
            response => {
                this.setState({fund: response.data})
                console.log('response from get-Foreign-Fund:');
                console.log(response);
                console.log("this.state.fund:");
                console.log(this.state.fund);
            }
        );

        // this.myChart = echarts.init(this.chart);
    }

    getTwoCompareOption = (x, y1, y2) => {
        let option={
            toolbox: {
                feature: {
                    dataView: {show: true, readOnly: true},
                    saveAsImage: {show: true}
                }
            },
            xAxis: {
                type: "category",
                data: x
            },
            yAxis: [{
                type: "value",
                name: "point",
                min: function (value) {
                    return Math.floor(value.min / 100) * 100;
                },
                max: function (value) {
                    return Math.ceil(value.max / 100 ) * 100;
                },
                axisLabel: {

                }
            }, {
                type: "value",
                name: "NT",
                min: function (value) {
                    return Math.floor(value.min / 100) * 100;
                },
                max: function (value) {
                    return Math.ceil(value.max / 100 ) * 100;
                },
                axisLabel: {
                    formatter: function (value) {
                        return parseInt(value/1000000000).toString() + ' B';
                    }
                }
            }],
            dataZoom: [{
                type: 'slider',
                start: 0,
                end: 100
            }, {
                start: 0,
                end: 100
            }],
            // showing each value by place the mouse on it
            tooltip: {
                order: 'valueDesc',
                    trigger: 'axis'
            },
            legend: {
                data: ['TAIEX Open', 'Foreign Fund Difference']
            },
            series: [
                {
                    name: "TAIEX Open",
                    data: y1,
                    type: "line",
                    emphasis: {
                        focus: 'series'
                    },
                    encode: {
                        tooltip: ['value']
                    }
                },
                {
                    name: "Foreign Fund Difference",
                    data: y2,
                    type: "line",
                    emphasis: {
                        focus: 'series'
                    },
                    encode: {
                        tooltip: ['value']
                    },
                    yAxisIndex: 1
                }
            ]
        }
        return option
    }

    render() {
        return (
            <div>
            <h1>
                Hello Piggy!
            </h1>
            <ReactEcharts
                option={this.getTwoCompareOption(this.state.TAIEX.x, this.state.TAIEX.y, this.state.fund.y)}
            />
            </div>
        )
    }
}
export default HomePage;