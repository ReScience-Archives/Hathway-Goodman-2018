from figure_1 import fig_1
from figure_2 import fig_2
from figure_5 import fig_5_saved, fig_5_new
from figure_6 import fig_6_saved, fig_6_new
from run_simulation import run_sim
from figure_7CD import fig_7CD
from figure_8 import fig_8
from write_param_inputfile import write_para_file
import matplotlib.pyplot as plt
import argparse
import time


# ### get command line options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--new", required=False, default='False',
	help="whether to run calculations for figures 5 and 6 (True) or use saved values (False, default)")
args = vars(ap.parse_args())


# ### plot figures from paper
fig1 = fig_1()


fig2 = fig_2()


print('%s Preparing Figures 3, 4, 7AB' % time.strftime('%H:%M'))
fig3, fig4, fig7AB = run_sim(0)


if args['new'] == 'False':
    fig5 = fig_5_saved()
    fig6 = fig_6_saved()

elif args['new'] == 'True':
    write_para_file()

    reps_per_combination = 1
    fig5 = fig_5_new(reps_per_combination)

    reps_per_resolution = 2
    fig6 = fig_6_new(reps_per_resolution)

else:
    'input for --new was not recognised. Please try again'


fig7CD = fig_7CD(3)


fig8 = fig_8()


plt.show()

