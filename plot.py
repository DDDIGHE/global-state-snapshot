import matplotlib.pyplot as plt

# 数据
branch_data = {
    3: {
        'transaction_intervals': [0.15, 0.2, 0.25, 0.3, 0.35, 0.4],
        'average_message_sizes': [130.83, 130.70, 130.63, 130.62, 130.60, 130.46],
        'messages_per_second': [12.69, 10.58, 8.91, 7.55, 6.59, 6.11],
        'total_storage_sizes': [3504, 3500, 3504, 3510, 3510, 3514],
        'average_storage_sizes': [1168, 1166.67, 1168, 1170, 1170, 1171.33],
        'throughputs': [12.69, 10.58, 8.91, 7.55, 6.59, 6.11],
        'average_snapshot_latencies': [9.08, 11.19, 17.71, 34.90, 33.04, 43.21],
        'snapshot_1_positions': [61, 57, 45, 54, 63, 55],
        'snapshot_1_durations': [6.3, 8.09, 4.19, 12.28, 18.39, 12.31],
        'snapshot_2_positions': [194, 205, 177, 308, 230, 305],
        'snapshot_2_durations': [8.99, 6.76, 0.91, 31.91, 14.07, 33.02],
        'snapshot_3_positions': [410, 556, 481, 929, 713, 1025],
        'snapshot_3_durations': [11.95, 18.73, 48.04, 60.52, 66.67, 84.3],
    },
    4: {
        'transaction_intervals': [0.15, 0.2, 0.25, 0.3, 0.35, 0.4],
        'average_message_sizes': [130.81, 130.75, 130.60, 130.58, 130.51, 130.43],
        'messages_per_second': [23.53, 20.14, 17.22, 14.92, 13.41, 11.78],
        'total_storage_sizes': [3855, 3856, 3865, 3870, 3879, 3881],
        'average_storage_sizes': [1285, 1285.33, 1288.33, 1290, 1293, 1293.67],
        'throughputs': [23.53, 20.14, 17.22, 14.92, 13.41, 11.78],
        'average_snapshot_latencies': [3.53, 7.96, 15.60, 29.38, 54.97, 69.45],
        'snapshot_1_positions': [73, 62, 88, 108, 126, 110],
        'snapshot_1_durations': [2.88, 4.69, 2.9, 9.54, 13.05, 10.25],
        'snapshot_2_positions': [497, 251, 497, 854, 610, 826],
        'snapshot_2_durations': [4.91, 6.73, 18.71, 8.28, 42.32, 64.81],
        'snapshot_3_positions': [787, 695, 1206, 2087, 2100, 2674],
        'snapshot_3_durations': [2.8, 12.45, 25.21, 70.33, 109.54, 133.27],
    }
}

# 定义绘图函数
def plot_graph(x_label, y_label, data_label, branch_data):
    plt.figure()
    for branch, data in branch_data.items():
        plt.plot(data['transaction_intervals'], data[data_label], label=f'Branch {branch}')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()
    
def plot_position_duration(data_label_position, data_label_duration, branch_data):
    plt.figure()
    for branch, data in branch_data.items():
        plt.scatter(data[data_label_position], data[data_label_duration], label=f'Branch {branch}')
    plt.xlabel('Position')
    plt.ylabel('Duration')
    plt.legend()
    plt.grid()
    plt.show()

# 绘制12张图
plot_graph('Transaction Interval', 'Average Message Size', 'average_message_sizes', branch_data)
plot_graph('Transaction Interval', 'Messages per Second', 'messages_per_second', branch_data)
plot_graph('Transaction Interval', 'Total Storage Size', 'total_storage_sizes', branch_data)
plot_graph('Transaction Interval', 'Average Storage Size', 'average_storage_sizes', branch_data)
plot_graph('Transaction Interval', 'Throughput', 'throughputs', branch_data)
plot_graph('Transaction Interval', 'Average Snapshot Latency', 'average_snapshot_latencies', branch_data)
plot_graph('Transaction Interval', 'Snapshot #1 Position', 'snapshot_1_positions', branch_data)
plot_graph('Transaction Interval', 'Snapshot #1 Duration', 'snapshot_1_durations', branch_data)
plot_graph('Transaction Interval', 'Snapshot #2 Position', 'snapshot_2_positions', branch_data)
plot_graph('Transaction Interval', 'Snapshot #2 Duration', 'snapshot_2_durations', branch_data)
plot_graph('Transaction Interval', 'Snapshot #3 Position', 'snapshot_3_positions', branch_data)
plot_graph('Transaction Interval', 'Snapshot #3 Duration', 'snapshot_3_durations', branch_data)
plot_position_duration('snapshot_1_positions', 'snapshot_1_durations', branch_data)
plot_position_duration('snapshot_2_positions', 'snapshot_2_durations', branch_data)
plot_position_duration('snapshot_3_positions', 'snapshot_3_durations', branch_data)
