%% Plotting humidity + temperature + power 
close all
clear all

pwh_data = readmatrix('pw_file11.csv');
time_ind = [1:length(pwh_data)];

temp = pwh_data(1,:);
rain = pwh_data(2,:);
wind = pwh_data(3,:);
humid = pwh_data(4,:);
power = pwh_data(5,:);

avg_power = movmean(power, 20);

figure

title('Environmental Temperature and RSS')
xlabel('Time (min)')
yyaxis left
%plot(time_ind, power)
hold on
plot(time_ind, avg_power )
ylabel('RSS (db)')
hold on
yyaxis right
plot(time_ind, temp)
ylabel('Temperature (C)')

figure
title('Rainfall and RSS')
xlabel('Time (min)')
yyaxis left
%plot(time_ind, power)
hold on
plot(time_ind, avg_power )
ylabel('RSS (db)')
hold on
yyaxis right
plot(time_ind, rain)
ylabel('Rainfall (cm)')


figure
title('Windspeed e and RSS')
xlabel('Time (min)')
yyaxis left
%plot(time_ind, power)
hold on
plot(time_ind, avg_power)
ylabel('RSS (db)')
hold on
yyaxis right
plot(time_ind, wind)
ylabel('Windspeed (m/s)')


figure
title('Humidity and RSS')
xlabel('Time (min)')
yyaxis left
%plot(time_ind, power)
hold on
plot(time_ind, avg_power)
ylabel('RSS (db)')
hold on
yyaxis right
plot(time_ind, humid)
ylabel('Humidity (%)')

%% Plotting individually

close all
clear all

pwh_data = readmatrix('pw_file11.csv');
time_ind = [1:length(pwh_data)];

temp = pwh_data(1,:);
rain = pwh_data(2,:);
wind = pwh_data(3,:);
humid = pwh_data(4,:);
power = pwh_data(5,:);

avg_power = movmean(power, 20);

figure
subplot(4, 1, 1)
plot(time_ind, avg_power)
ylabel('RSS (dB, unknown reference)')
title('Received Signal Strength')
xlabel('Time (min)')


subplot(4, 1, 2)
plot(time_ind, temp)
ylabel('Temperature (C)')
title('Environmental Temperature')
xlabel('Time (min)')

subplot(4, 1, 3)
plot(time_ind, humid)
ylabel('Humidity (%)')
title('Humidity')
xlabel('Time (min)')

subplot(4, 1, 4)
plot(time_ind, wind)
ylabel('Windspeed (m/s)')
title('Wind Speed')
xlabel('Time (min)')

figure 
subplot(2,1,1)
plot(time_ind, avg_power)
ylabel('RSS (dB) (unknown reference)')
title('Received Signal Strength')
xlabel('Time (min)')

hold on
subplot(2,1,2)
plot(time_ind, wind)
ylabel('Wind Speed (m/s)')
title('Wind Speed')
xlabel('Time (min)')

figure 
subplot(2,1,1)
plot(time_ind, avg_power)
ylabel('RSS (dB) (unknown reference)')
title('Received Signal Strength')
xlabel('Time (min)')

hold on
subplot(2,1,2)
plot(time_ind, rain)
ylabel('Rainfall')
title('Rainfall')
xlabel('Time (min)')

figure 
subplot(2,1,1)
plot(time_ind, avg_power)
ylabel('RSS (dB) (unknown reference)')
title('Received Signal Strength')
xlabel('Time (min)')

hold on
subplot(2,1,2)
plot(time_ind, humid)
ylabel('Humidity (%)')
title('Humidity')
xlabel('Time (min)')

figure 
subplot(2,1,1)
plot(time_ind, avg_power)
ylabel('RSS (dB) (unknown reference)')
title('Received Signal Strength')
xlabel('Time (min)')

hold on
subplot(2,1,2)
plot(time_ind, temp)
ylabel('Temperature (C)')
title('Temperature')
xlabel('Time (min)')



