import React from "react";
// import * as echarts from "echarts";
import axios from "axios";
import ReactEcharts from "echarts-for-react"

class HomePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {TAIEX: {}};
        this.chart = null;
    }

    componentDidMount() {
        axios.get('/api/get-TAIEX').then(
            response => {
                this.setState({TAIEX: response.data})
                console.log(response);
                console.log(this.state.TAIEX);
            }
        )

        // this.myChart = echarts.init(this.chart);
    }

    render() {
        return (
            <div>
            <h1>
                Hello Pig!
            </h1>
            <ReactEcharts
                option={{
                    xAxis: {
                        type: "category",
                        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    },
                    yAxis: {
                        type: "value"
                    },
                    tooltip: {
                        order: 'valueDesc',
                        trigger: 'axis'
                    },
                    series: [{
                        data: [5, 15, 33, 46, 1, 17, 36],
                        type: "line",
                        labelLayout: {
                            moveOverlap: 'shifY'
                        },
                        emphasis: {
                            focus: 'series'
                        },
                        encode: {
                            tooltip: ['value']
                        }
                    }]
                }}
            />
            </div>
        )
    }
}
export default HomePage;