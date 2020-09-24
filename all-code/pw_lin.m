%% Finding a Linear Relationship between Temperature and Power


% tx: MEB
% rx: USTAR

pw_data1 = readmatrix('pw_file8.csv');
pw_data2 = readmatrix('pw_file9.csv');
pw_data = [pw_data1, pw_data2];

temp_rss = pw_data([1,4],:);
temp = pw_data(1,:);

[sorted_temp, I] = sort(temp);

len = length(I);
sorted = zeros(2, len);
for n = 1 : len
    index = I(n);
    values = temp_rss(:,index);
    sorted(:,n) = values;
end 
    
%temp_avg = movmean(sorted(2,:),15);
figure
scatter(sorted(1,:), temp_avg, 5)
scatter(sorted(1,:), sorted(2,:), 5)
xlabel('Temperature (K)')
ylabel('Recieved Signal Strength (dB)')
title('Temperature and Time')

%% Attempting to gather all power values with same temperature

totals = zeros(len);

num = 1;
for m = 1 : len-1
    if sorted(1,m) == sorted(1,m+1)
        totals(1,m) = sorted(1,m);
        totals(num+2,m) = sorted(2,m);
        num = num + 1;
    else 
        totals(2,m) = num;
        num = 1;
        totals(1,m) = sorted(1,m);
        totals(num+2,m) = sorted(2,m);
    end
end


    