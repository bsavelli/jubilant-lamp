Graphing interface data


import pygal


#SNMP datas that need to be graphed on a line chart


line_chart = pygal.Line()

line_chart.title = 'Input/Output Packets and Bytes'
line_chart.x_labels = ['5','10','15','20','25','30','35','40','45','50','55','60']
line_chart.add('InPackets', <<variable data list>>)


rinse and repeat




line_chart.render_to_file('test_svg')


