# This entrypoint file to be used in development. Start by reading README.md
# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and save the categorical plot
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig("catplot.png")

# Generate and save the heat map
heat_map_fig = draw_heat_map()
heat_map_fig.savefig("heatmap.png")


# Run unit tests automatically
#main(module='test_module', exit=False)