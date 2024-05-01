--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cafeteria; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cafeteria (
    id_cafeteria integer,
    nome_cafeteria character varying(50),
    telefone character(11),
    endereco character varying(50)
);


--
-- Name: pedido; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pedido (
    id_pedido integer NOT NULL,
    id_cafeteria integer NOT NULL,
    pedido_nome integer NOT NULL,
    pedido_quantidade integer NOT NULL,
    id_produto integer,
    id_usuario integer
);


--
-- Name: produto; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.produto (
    id_produto integer NOT NULL,
    id_cafeteria integer,
    nome_produto character varying(50) NOT NULL,
    preco double precision NOT NULL
);


--
-- Name: produtomaisvendido; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.produtomaisvendido (
    id_cafeteria integer NOT NULL,
    nome_cafeteria character varying(50),
    id_produto_mais_vendido integer,
    nome_produto_mais_vendido character varying(50),
    total_vendas integer
);


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    nome_usuario character varying(15) NOT NULL,
    telefone character(11) NOT NULL,
    endereco character varying(50)
);


--
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id_pedido);


--
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id_produto);


--
-- Name: produtomaisvendido produtomaisvendido_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.produtomaisvendido
    ADD CONSTRAINT produtomaisvendido_pkey PRIMARY KEY (id_cafeteria);


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);


--
-- PostgreSQL database dump complete
--

