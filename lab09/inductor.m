function [l,r] = inductor(l,r)
    h = tf([0 r],[l r]);
    bode(h);
    hold on;
    h = tf([0 r*0.5],[l r*0.5]);
    bode(h);
    hold on;
    
    h = tf([0 r*2],[l r*2]);
    bode(h);
    hold on;
end