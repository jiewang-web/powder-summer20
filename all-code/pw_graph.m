%% Graphing Temperature and Received Signal Strength
close all;
clear all;

% pw_file8: tx-MEB rx-USTAR
pw_data = readmatrix('pw_file8.csv');

time_ind = [1:length(pw_data)];
temp_data = pw_data(1,:);
%humid_data = pw_data(4,:);
rss_data = pw_data(4,:);

%plot
figure
title('Temperature and Recieved Signal Strength')
xlabel('Time (~minutes)')
yyaxis left
plot(time_ind, temp_data)
ylabel('Temperature (K)')
hold on
yyaxis right
plot(time_ind, rss_data)
ylabel('RSS (dB) (unknown reference)')

%moving mean of RSS
avg_rss = movmean(rss_data, 15);
figure
title('Temperature and Recieved Signal Strength (Avg)')
xlabel('Time (~minutes)')
yyaxis left
plot(time_ind, temp_data)
ylabel('Temperature (K)')
hold on
yyaxis right
plot(time_ind, avg_rss)
ylabel('RSS (dB) (unknown reference)')

% humidity plot
%figure
%title('Environmental Humidity (%)')
%xlabel('Time (~minutes)')
%yyaxis left
%plot(time_ind, humid_data)
%ylabel('Humidity (%)')
%hold on
%yyaxis right
%plot(time_ind, avg_rss)
%ylabel('RSS (dB)')






