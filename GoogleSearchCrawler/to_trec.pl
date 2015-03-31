#!/usr/bin/perl -w

my $usage = "perl $0 input output\n";
my $input = shift @ARGV or die $usage;
my $output = shift @ARGV or die $usage;
foreach (1..60) {
    print "process query $_\n";
    open FH, "$input/$_.res" or die $!;
    open OUT, ">$output/$_.trec" or die $!;

    $counter = 0;
    print OUT "<DOCNO>$_</DOCNO>\n";
    print OUT "<TEXT>\n";
    while (<FH>) {
        $counter += 1;
        print OUT substr(<FH>, 7), substr(<FH>, 9);
        last if $counter == 3;
    }
    print OUT "</TEXT>\n";
    close FH;
    close OUT;
}
