#!/usr/bin/env ruby
ARGV[0].scan(/^hbt*n$/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
