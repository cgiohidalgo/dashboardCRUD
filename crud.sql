PGDMP         4                z            crud    12.12    15.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16516    crud    DATABASE     z   CREATE DATABASE crud WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE crud;
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false                       0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    6            ?            1259    16519    personas    TABLE     ?   CREATE TABLE public.personas (
    idper smallint NOT NULL,
    cedula character varying(11) NOT NULL,
    nombre character varying(60) NOT NULL
);
    DROP TABLE public.personas;
       public         heap    postgres    false    6            ?            1259    16517    personas_idper_seq    SEQUENCE     ?   CREATE SEQUENCE public.personas_idper_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.personas_idper_seq;
       public          postgres    false    6    203            	           0    0    personas_idper_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.personas_idper_seq OWNED BY public.personas.idper;
          public          postgres    false    202            
           2604    16522    personas idper    DEFAULT     p   ALTER TABLE ONLY public.personas ALTER COLUMN idper SET DEFAULT nextval('public.personas_idper_seq'::regclass);
 =   ALTER TABLE public.personas ALTER COLUMN idper DROP DEFAULT;
       public          postgres    false    202    203    203                      0    16519    personas 
   TABLE DATA           9   COPY public.personas (idper, cedula, nombre) FROM stdin;
    public          postgres    false    203   k       
           0    0    personas_idper_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.personas_idper_seq', 7, true);
          public          postgres    false    202            ?
           2606    16524    personas personas_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.personas
    ADD CONSTRAINT personas_pkey PRIMARY KEY (idper);
 @   ALTER TABLE ONLY public.personas DROP CONSTRAINT personas_pkey;
       public            postgres    false    203               _   x?3?4?042046??*M?SpN,??/V?MM??K?2?4442?052?4??t?KT?M,:?6?ˈ????????(?R?????Z?????Z????? '?     