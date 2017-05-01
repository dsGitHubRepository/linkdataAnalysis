% Q2.m

% clc;clear all;close all;
% parameter L9, L19

 function [probabilityGT]=Q1()
 
 Nite=2000; % 5000; % No of iterations; the higher the better
 payments=zeros(1,Nite);
 for ite=1:Nite
     totalpayment=mean_std_totPayments(20);  % N=10 or 20
     payments(ite)=totalpayment;
 end
 paymentsdist=sort(payments,'descend');
 Normalizedpaymentsdist=paymentsdist/sum(paymentsdist);
 
 close all;plot(Normalizedpaymentsdist,'dk--');
 set(gca,'FontSize', 20);
 title('Cumulative probability')
 
 
 totProb=sum(Normalizedpaymentsdist);
 
 % payment is greater than or equal to 45 for N=10 OR 160 for N=20

cutoff=160;  % cutoff=45 or 160

paymentsdistGT=sort(paymentsdist(paymentsdist >= cutoff));
Normalized_paymentsdistGT=paymentsdistGT/sum(paymentsdist);
probabilityGT=sum(Normalized_paymentsdistGT);

fprintf('probability total payment >= cutoff for N : %1.10f\n',probabilityGT)
return
  
 
function [totalpayment]=mean_std_totPayments(N)

% N=10;
coins=1:N;  % N=10 or 20 etc

randomPicks=zeros(1,N);
for i=1:N
    coinPick=randsample(coins,1);
    randomPicks(i)=coinPick; 
    ind=find(coins==coinPick);
    coins(ind)=[]; % since coins are drawn iteratively without repalceemnt
end

% are paid the absolute difference between the drawn coin and the
% previously drawn coins

price=zeros(1,size(randomPicks,2)-1);
for j=1:size(randomPicks,2)-1
    if (j==1)
        p=randomPicks(j);
    else
        p=abs(randomPicks(j)-randomPicks(j-1));
    end
    price(j)=p;
end

meanpayment=mean(price);
stddeviation=std(price);

%fprintf('value of meanpayment is %1.10f\n',meanpayment);

%fprintf('standard deviation is %1.10f\n', stddeviation);

totalpayment=sum(price);
return



