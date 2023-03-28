#!/usr/bin/env ruby
ARGV[0].scan(/^\d\d\d\d\d\d\d\d\d\d$/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
