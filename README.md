# Quick_RSA
Quick rsa through console, requires Python 3.x <br>
Currently not available through pip.

Currenly only working with  <code>python3 rsa_decoder.py</code>  command <br>

# Help

```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py --help
usage: rsa_decoder.py [-h] {gkey,decode,encode} ...

RSA decoder, encoder

positional arguments:
  {gkey,decode,encode}  sub-command help
    gkey                Helps you to create key
    decode              Decode files
    encode              b help

optional arguments:
  -h, --help            show this help message and exit
```
<h3> Generate keys: </h3>
```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py gkey --help
usage: rsa_decoder.py gkey [-h] [--bsize BSIZE] [--overwrite]
                           [--filepath FPATH] [--filename FNAME]

optional arguments:
  -h, --help            show this help message and exit
  --bsize BSIZE, -s BSIZE
                        Byte size for key
  --overwrite, -o       Whether overwrite file or not
  --filepath FPATH, -f FPATH
                        File path to be saved
  --filename FNAME, -n FNAME
                        File name to be saved, w/o extension


```
<h3> Encrypt file: </h3>
```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py encode --help
usage: rsa_decoder.py encode [-h] [--infile INFILE] [--publickey PUBLICKEY]

optional arguments:
  -h, --help            show this help message and exit
  --infile INFILE, -f INFILE
                        File location , name , extension
  --publickey PUBLICKEY, -p PUBLICKEY
                        Public key location , name , extension

```
<h3> Decrypt file: </h3>
```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py decode --help
usage: rsa_decoder.py decode [-h] [--infile INFILE] [--privatekey PRIVATEKEY]

optional arguments:
  -h, --help            show this help message and exit
  --infile INFILE, -f INFILE
                        File location , name , extension
  --privatekey PRIVATEKEY, -p PRIVATEKEY
                        Private key location , name , extension
```


# Examples
Generate a 2048 key in Desktop:
```{r, engine='sh', count_lines=true}
$python3 rsa_decoder.py gkey -s 2048 -f ~/Desktop -n mytestkey.pem
```
<h4>
Output: <br>public key --> mytestkey.pem <br>
        private key -> pv_mytestkey.pem <br>
</h4>

##### Created an example file named mysecret.txt

```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py encode -f ~/Desktop/mysecret.txt -p ~/Desktop/mytestkey.pem
```
#### This should create a file named mysecret.txt_out in Desktop. If you open it you can see encrypted text.

### Now, let's decode the file using private key.

```{r, engine='sh', count_lines=true}
$ python3 rsa_decoder.py decode -f ~/Desktop/mysecret.txt_out -p ~/Desktop/pv_mytestkey.pem
```

#### Than it should create a file named mysecret.txt_out_out with proper text ( decrypted with private key )
##
#
![Image from couple testigs](https://i.imgur.com/ua9xxB0.jpg?1)
#
## Output file option will be available in a week.
#### <a href="www.dogacel.com">Dogacel.com &copy;</a>

