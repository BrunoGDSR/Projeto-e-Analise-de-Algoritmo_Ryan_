import 'package:flutter/material.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _emailController = TextEditingController();
  final _senhaController = TextEditingController();

  bool get _camposPreenchidos =>
      _emailController.text.isNotEmpty && _senhaController.text.isNotEmpty;

  @override
  Widget build(BuildContext context) {

    final colorScheme = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
       
      ),
      body: Padding(
        padding: const EdgeInsets.all(30),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
         
            Icon(
              Icons.lock_person_outlined,
              size: 80,
              color: colorScheme.primary, 
            ),
            const SizedBox(height: 40),
            
            
            TextField(
              controller: _emailController,
              decoration: InputDecoration(
                icon: Icon(Icons.email, color: colorScheme.primary), 
                hintText: 'Digite seu email',
                labelText: 'Email',
                border: const OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12))), 
              ),
              onChanged: (_) => setState(() {}),
            ),
            const SizedBox(height: 20),
            TextField(
              controller: _senhaController,
              obscureText: true,
              decoration: InputDecoration(
                icon: Icon(Icons.lock, color: colorScheme.primary), 
                hintText: 'Digite sua senha',
                labelText: 'Senha',
                border: const OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12))), 
              ),
              onChanged: (_) => setState(() {}),
            ),
            const SizedBox(height: 40),
            
            
            ElevatedButton(
              onPressed: _camposPreenchidos ? () {} : null,
              child: const Text(
                'Entrar',
                style: TextStyle(fontSize: 16),
              ),
            ),
            
          
            TextButton(
              onPressed: () {},
              child: const Text('Esqueceu a senha?'),
            ),
          ],
        ),
      ),
    );
  }
}