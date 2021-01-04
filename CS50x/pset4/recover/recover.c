#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define NUMBYTES 512

int main(int argc, char *argv[])
{
    // check usage of command line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // open file and check if works
    FILE *inFile = fopen(argv[1], "r");
    if (inFile  == NULL)
    {
        printf("File could not be opened.");
        return 1;
    }

    // file ptr to write to
    FILE *outFile = NULL;

    // define BYTE to use
    typedef uint8_t BYTE;

    // buffer array, array to store header (to check), JPG header array to compare
    BYTE buffer[NUMBYTES], header[4], JPGheader[4] = {0xff, 0xd8, 0xff, 0xe0};

    // bytesRead to compare fread() return and numJPGs to add into for files
    int bytesRead, numJPGs = 0;

    // array to store file name
    char jpgFile[8];

    while (fread(&buffer, NUMBYTES, 1, inFile) > 0)
    {
        // first 4 bytes match JPG header options
        if (buffer[0] == JPGheader[0] && buffer[1] == JPGheader[1] && buffer[2] == JPGheader[2] && (buffer[3] & 0xf0) == JPGheader[3])
        {
            if (outFile != NULL)
            {
                fclose(outFile);
                numJPGs++;
            }
            sprintf(jpgFile, "%03i.jpg", numJPGs);
            outFile = fopen(jpgFile, "w");
            fwrite(&buffer, NUMBYTES, 1, outFile);
        }
        // not the start of JPG file
        else
        {
            // file already open => continue writing block to file
            if (outFile != NULL)
            {
                fwrite(&buffer, NUMBYTES, 1, outFile);
            }
        }
    }


    fclose(inFile);
    fclose(outFile);
}