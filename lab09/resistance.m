function [r,c] = resistance(r,c)
 h = tf([1 0],[0 1 1/(r*c)]);
 bode(h);
hold on;
h = tf([1 0],[0 1 1/(r*0.5*c)]);
bode(h);
hold on;
h = tf([1 0],[0 1 1/(r*2*c)]);
bode(h);
hold on;
h = tf([1 0],[0 1 1/(r*2*c)]);
bode(h);
end