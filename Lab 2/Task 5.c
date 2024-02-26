#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
#include <termios.h>
#include <sys/select.h>

void time_handler(int signum) {
    static int count = 0;
    struct timeval ts;
    
    count++;
    gettimeofday(&ts, NULL);
    printf("%d.%06d : timer expired %d times\n", ts.tv_sec, ts.tv_usec, count);
}

struct termios orig_term;

void setup_terminal() {
    struct termios new_term;
    tcgetattr(STDIN_FILENO, &orig_term);
    new_term = orig_term;
    new_term.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &new_term);
}

void restore_terminal() {
    tcsetattr(STDIN_FILENO, TCSANOW, &orig_term);
}

int main() {
    struct sigaction sa;
    struct itimerval timer;

    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = &time_handler;
    sigaction(SIGVTALRM, &sa, NULL);

    timer.it_value.tv_sec = 0;
    timer.it_value.tv_usec = 500000;
    timer.it_interval.tv_sec = 0;
    timer.it_interval.tv_usec = 500000;
    setitimer(ITIMER_VIRTUAL, &timer, NULL);

    setup_terminal();

    fd_set readfds;
    int result;

    // Main loop
    while(1) {
        FD_ZERO(&readfds);
        FD_SET(STDIN_FILENO, &readfds);
        
        // Set timeout to zero to make select non-blocking
        struct timeval tv;
        tv.tv_sec = 0;
        tv.tv_usec = 0;

        result = select(STDIN_FILENO + 1, &readfds, NULL, NULL, &tv);

        // Check if select() indicated that data is ready to read
        if (result > 0) {
            char ch;
            read(STDIN_FILENO, &ch, 1);
            if (ch == 'A' || ch == 'a') {
                printf("A was pressed - exiting.\n");
                break;
            }
        }
    }

    restore_terminal();

    return 0;
}
