function [r,l,c] = rlc(r,l,c)
    h = tf([r 0],[l r 1/c]);
    bode(h);
end
