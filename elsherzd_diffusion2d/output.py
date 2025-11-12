import matplotlib.pyplot as plt


def create_plot(fig, subplot_num, u, time_ms, T_cold, T_hot):
    ax = fig.add_subplot(subplot_num)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(time_ms))
    return im


def output_plots(fig, im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

