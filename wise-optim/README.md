# Wise Optimization - Project - Rohan Kotwani

There are two data sources that were used: 1) the previous running order of cars (what place they are in) for each lap and 2) the statistics by car and lap at each chose cone.

The choice cone is the lap where the caution flag turns from yellow to green. At this point, the driver can decide to either take the inner or outer side of the track. While the outer side might be preferable, the inner side can increase the short term position of a driver.

Here we see the previous running order was 6, 77, 54… And we see that driver 6 went to the outer side of the track while driver 77 went to the inner side. Whether the driver went inner/outer is the line up order.

![example.png](example.png)

For example, at the beginning of the lap, for when the flag turns from yellow to green at the end of the lap, marks the previous running order.

Since the data is recorded at the end of the lap, if the flag changes to green on lap 35, then the running order at lap 34 will show the previous running order.

Next, the driver's choice of inner or outer is determined by measuring their distance to the wall, when the flag turns green, at the start of the next lap (say lap 36).

A statistical model to divide the group of cars by distance to the wall. I excluded any cars more than 95 feet from the wall and recorded them as pit stops.

![graph.png](graph.png)

This has the benefit of assigning some uncertainty to the categories, but, also, it can possibly be used to find restart periods.

After categorizing each driver into the inner/outer category, the next step was to find the line up order. This was done by 1) sorting the drivers by the running order of the lap where the caution period ends and 2) splitting and then stacking the drivers who went 1) inner and 2) outer, side by side.

However, it is unclear if the previous running order should show drivers that are not in the top 16 line-up after the green flag.

For example, here is the order on lap 60, the end of the caution period:

```
22 2 21 48 19 47 7 17 34 71 6 11 1 12 42 38
```

Car 6 and 12 are not in the top 16 line up for the restart. But they are in the running order after the restart.

# Here were my initial thoughts before seeing the data or project

## Objective

assuming you want the green flag to position -> to analyze the positive and negative outcomes

## Analytics

Does the choice of left/right on a restart have some effect? Is it a psychological effect?
Do the previous lap positions effect the outcome? Did the driver have an intense overtaking lap?
Does a the choices of the cars that are behind/ahead have some influence? Is there a strategic advantage?
Is there a vehicle specification that leads to better outcomes with left/right choices?

## Data

The telemetry data and GPS data can be used to collect a series of data for lap positions and other factors.

Driver feedback can be incorporated (a rating of 1-10) to filter out false positives.

For noisy/dropped GPS data, there are simple to complex solutions. Vehicle tracking from broadcasts would be the most complex (unrecommended due to blurr and similarities between vehicles). Vehicle positions can be estimated with previous speeds and position along the track. A solution could be fine-tuned further with lap positions (either from a data source of extract from the broadcast). Extracting lap positions from the broadcast can be a consistent solution*.

## Models

Models can serve two purposes: 1) to speed up analysis 2) to predict some outcome 3) to explain some behavior 4) to produce higher quality data

Is there automatic green flag extraction? 
Is there a way to track vehicle positions with rarely dropped GPS data (this is important for a predictive solution).
Is there a better data source than the broadcast? If not, video processing to remove the commentary sections is a small but useful step.


However, an finetuned vehicle detection model can be trained for this dataset! The would entail building a large dataset with a data annotation tool. The solution would also need to map vehicles to driver vehicles based on the visual aspects of the car.
