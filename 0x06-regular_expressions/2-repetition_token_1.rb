#!/usr/bin/env ruby
ARGV[0].scan(/^hb{0,1}tn$/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
