===========
paretochart
===========

`Pareto chart`_ for python (similar to `Matlab`_, but much more flexible).

Features
--------

- **Data labels** for the chart x-axis.
- **Fully customizable** with unique ``arg`` and ``kwarg`` inputs:
   - *Bar chart*: follows the inputs of the `matplotlib.pyplot.bar`_ 
     function (use ``bar_args=(...)`` and ``bar_kw={...}``).
   - *Cumulative line*: follows the inputs of the `matplotlib.pyplot.plot`_ 
     function (use ``line_args=(...)`` and ``line_kw={...}``).
   - *Limit line*: follows the inputs of the `matplotlib.axes.Axes.axhline`_ 
     function (use ``limit_kw={...}``).
- Put the chart on **arbitrary axes**.

Examples
--------
First, a simple import::
     
    from paretochart import pareto

Now, let's create the numeric data (no pre-sorting necessary)::

    data = [21, 2, 10, 4, 16]
     
We can even assign x-axis labels (in the same order as the data)::

    labels = ['tom', 'betty', 'alyson', 'john', 'bob']

For this example, we'll create 4 plots that show the customization 
capabilities::

    import matplotlib.pyplot as plt

    # create a grid of subplots
    fig, axes = plt.subplots(2, 2)
    
The first plot will be the simplest usage, with just the data::
    
    pareto(data, axes=axes[0, 0])
    plt.title('Basic chart without labels', fontsize=10)
    
In the second plot, we'll add labels, put a cumulative limit at 0.75 (or 75%) 
and turn the cumulative line green::

    pareto(data, labels, axes=axes[0, 1], limit=0.75, line_args=('g',))
    plt.title('Data with labels, green cum. line, limit=0.75', fontsize=10)
    
In the third plot, we'll remove the cumulative line and limit line, make the
bars green and resize them to a width of 0.5::

    pareto(data, labels, cumplot=False, axes=axes[1, 0], data_kw={'width': 0.5,
        'color': 'g'})
    plt.title('Data without cum. line, green bar width=0.5', fontsize=10)
    
In the fourth plot, let's put the cumulative limit at 95% and make that line
yellow::

    pareto(data, labels, limit=0.95, axes=axes[1, 1], limit_kw={'color': 'y'})
    plt.title('Data trimmed at 95%, yellow limit line', fontsize=10)

And last, but not least, let's show the image::

    fig.canvas.set_window_title('Pareto Plot Test Figure')
    plt.show()

This should result in the following image (`click here`_ if the image doesn't 
show up):

.. image:: https://raw.github.com/tisimst/paretochart/master/pareto_plot_test_figure.png
   :scale: 75%

Installation
------------

Since this is really a single python file, you can simply go to the 
GitHub_ page, simply download ``paretochart.py`` and put it in 
a directory that python can find it.

Alternatively, the file can be installed using::

    $ pip install --upgrade paretochart

or::
    
    $ easy_install --upgrade paretochart

If you are using Python3, download the compressed file from here, unzip and run::

    $ 2to3 -w *.py
    
while in the unzipped directory, *then* run::

    $ python3 setup.py install

**NOTE:** *Administrative privileges may be required to perform any of 
the above install methods.*

Contact
-------

Please send **feature requests, bug reports, or feedback** to `Abraham Lee`_.

.. _Pareto chart: http://en.wikipedia.org/wiki/Pareto_chart
.. _Matlab: http://www.mathworks.com/help/matlab/ref/pareto.html
.. _matplotlib.pyplot.bar: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
.. _matplotlib.pyplot.plot: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
.. _matplotlib.axes.Axes.axhline: http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.axhline
.. _Abraham Lee: mailto:tisimst@gmail.com
.. _GitHub: https://github.com/tisimst/paretochart
.. _click here: https://github.com/tisimst/paretochart/master/pareto_plot_test_figure.png
