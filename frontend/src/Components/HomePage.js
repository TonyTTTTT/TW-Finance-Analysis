import React from "react";
// import * as echarts from "echarts";
import axios from "axios";
import ReactEcharts from "echarts-for-react";
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';


const apiUrl = 'http://linux8.csie.ntu.edu.tw:5050'
class HomePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            TAIEX: {},
            fund: {},
            TAIEX_Diff: {},
            value: 1
        };
        this.chart = null;
    }

    componentDidMount() {
        axios.get(`${apiUrl}/get-TAIEX`).then(
            response => {
                this.setState({TAIEX: response.data})
                console.log('response from get-TAIEX:');
                console.log(response);
                console.log("this.state.TAIEX:");
                console.log(this.state.TAIEX);
            }
        );

        axios.get(`${apiUrl}/get-TAIEX-Diff`).then(
            response => {
                this.setState({TAIEX_Diff: response.data})
                console.log('response from get-TAIEX-Diff:');
                console.log(response);
                console.log("this.state.TAIEX_Diff:");
                console.log(this.state.TAIEX_Diff);
            }
        );

        axios.get(`${apiUrl}/get-Foreign-Fund`).then(
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

    getTwoCompareOption = (x, y1, y2, x_name, y_name) => {
        let option={
            toolbox: {
                feature: {
                    dataView: {show: true, readOnly: true},
                    saveAsImage: {show: true}
                }
            },
            xAxis: {
                type: "category",
                data: x,
                axisLabel: {
                    formatter: function (value) {
                        return parseFloat(value).toString();
                    }
                }
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
                data: [x_name, y_name]
            },
            series: [
                {
                    name: x_name,
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
                    name: y_name,
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
            <Box sx={{ width: '100%', typography: 'body1' }}>
                <TabContext value={this.state.value}>
                    <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                        <TabList onChange={(e, newValue) => this.setState({ value: this.state.value = newValue})} centered>
                            <Tab label="Chart1" value="1" />
                            <Tab label="Chart2" value="2" />
                            <Tab label="TBD" value="3" />
                        </TabList>
                    </Box>
                    <TabPanel value="2">
                        <ReactEcharts
                            option={this.getTwoCompareOption(this.state.TAIEX_Diff.x, this.state.TAIEX_Diff.y, this.state.fund.y, "TAIEX Open's Diff", "Yesterday's Foreign Fund Diff")}
                        />
                    </TabPanel>
                    <TabPanel value="1">
                        <ReactEcharts
                            option={this.getTwoCompareOption(this.state.TAIEX.x, this.state.TAIEX.y, this.state.fund.y, "TAIEX Open", "Yesterday's Foreign Fund Diff")}
                        />
                    </TabPanel>
                    <TabPanel value="3">
                        <h1>Hello Cub!</h1>
                    </TabPanel>
                </TabContext>
            </Box>
        )
    }
}
export default HomePage;