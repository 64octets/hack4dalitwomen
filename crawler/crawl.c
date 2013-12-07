/*
 * This code is mostly taken from stackoverflow.com
 * The author is not very happy with this c code doing
 * a thing that can be done much more simply in python
 *
 * TODO: This is to be moved in python which the author
 * aspires to learn soon.
 *
 * Author: Satabdi Das
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "curl/curl.h"

struct string {
        char *ptr;
        size_t len;
};

void init_string(struct string *s) {
        s->len = 0;
        s->ptr = malloc(s->len+1);
        if (s->ptr == NULL) {
                fprintf(stderr, "malloc() failed\n");
                exit(EXIT_FAILURE);
        }
        s->ptr[0] = '\0';
}

size_t writefunc(void *ptr, size_t size, size_t nmemb, struct string *s)
{
        size_t new_len = s->len + size*nmemb;
        s->ptr = realloc(s->ptr, new_len+1);
        if (s->ptr == NULL) {
                fprintf(stderr, "realloc() failed\n");
                exit(EXIT_FAILURE);
        }
        memcpy(s->ptr+s->len, ptr, size*nmemb);
        s->ptr[new_len] = '\0';
        s->len = new_len;

        return size*nmemb;
}


int main (int argc, char* argv[])
{
        char *url = "http://access.alchemyapi.com/calls/url/URLGetText?apikey=7099dd459ad18fb49672e969d398119e3ad519d0&outputMode=json&extractLinks=1&url=";
        char final_url[2056];
        CURL *curl;
        CURLcode res;
  
      /* First some checks on arguments*/
        if (argc != 2) {
                printf ("Wrong number of arguments. Please provide - \"./crawl <url>\"\n");
                return -1;
        }
        sprintf(final_url, "%s%s", url, argv[1]);
        curl = curl_easy_init();
        if (curl) {
                struct string s;
                init_string(&s);

                curl_easy_setopt(curl, CURLOPT_URL, final_url);
                curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
                curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc   ); 
                curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);
                /* Perform the request, res will get the return code */ 
                res = curl_easy_perform(curl);
                /* Check for errors */ 
                if(res != CURLE_OK)
                        fprintf(stderr, "curl_easy_perform() failed: %s\n",
                                curl_easy_strerror(res));
 
                printf("%s\n", s.ptr);
                free(s.ptr);
                /* always cleanup */ 
                curl_easy_cleanup(curl);
        }
        return 0;
}
